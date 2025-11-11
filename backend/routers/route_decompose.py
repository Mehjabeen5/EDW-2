from fastapi import APIRouter
import re, uuid
from backend.schemas import RouteRequest, RouteResponse, DecomposeResponse, SubQuestion

router = APIRouter(prefix="/route", tags=["routing"])
REASONING_PAT = re.compile(r"\b(why|cause|reason|decline|drop|drivers?)\b", re.I)

@router.post("", response_model=RouteResponse)
def route(req: RouteRequest) -> RouteResponse:
    q = (req.question or "").strip()
    return RouteResponse(type="reasoning" if REASONING_PAT.search(q) else "basic")

@router.post("/decompose", response_model=DecomposeResponse)
def decompose(req: RouteRequest) -> DecomposeResponse:
    def sid() -> str: return uuid.uuid4().hex[:6]
    sq = [
        SubQuestion(id=f"q_time_{sid()}",    dimension="time",
                    nlq="Analyze revenue QoQ across last two quarters."),
        SubQuestion(id=f"q_region_{sid()}",  dimension="region",
                    nlq="Compare revenue by region across the last quarter."),
        SubQuestion(id=f"q_product_{sid()}", dimension="product",
                    nlq="Compare revenue by product line for the last quarter."),
        SubQuestion(id=f"q_orders_{sid()}",  dimension="orders",
                    nlq="Analyze order volume and average order value QoQ."),
    ]
    return DecomposeResponse(sub_questions=sq)

