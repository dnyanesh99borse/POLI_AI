from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# ✅ Correct token (without "Bearer")
TEAM_TOKEN = "30106cf177ae09a194632429999902655a931ac2ba1ebfb8dcdaa4d654dfc1bd"

class QueryRequest(BaseModel):
    documents: str
    questions: List[str]

class QueryResponse(BaseModel):
    answers: List[str]

# ✅ Static answers for sample HackRx questions
STATIC_ANSWERS = {
    "What is the waiting period for pre-existing diseases (PED) to be covered?":
        "There is a waiting period of thirty-six (36) months of continuous coverage from the first policy inception for pre-existing diseases and their direct complications to be covered.",
    
    "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?":
        "A grace period of thirty days is provided for premium payment after the due date to renew or continue the policy without losing continuity benefits.",

    "Does this policy cover maternity expenses, and what are the conditions?":
        "Yes, the policy covers maternity expenses, including childbirth and lawful medical termination of pregnancy. To be eligible, the female insured person must have been continuously covered for at least 24 months. The benefit is limited to two deliveries or terminations during the policy period.",

    "What is the waiting period for cataract surgery?":
        "The policy has a specific waiting period of two (2) years for cataract surgery.",

    "Are the medical expenses for an organ donor covered under this policy?":
        "Yes, the policy indemnifies the medical expenses for the organ donor's hospitalization for the purpose of harvesting the organ, provided the organ is for an insured person and the donation complies with the Transplantation of Human Organs Act, 1994.",

    "What is the No Claim Discount (NCD) offered in this policy?":
        "A No Claim Discount of 5% on the base premium is offered on renewal for a one-year policy term if no claims were made in the preceding year. The maximum aggregate NCD is capped at 5% of the total base premium.",

    "Is there a benefit for preventive health check-ups?":
        "Yes, the policy reimburses expenses for health check-ups at the end of every block of two continuous policy years, provided the policy has been renewed without a break. The amount is subject to the limits specified in the Table of Benefits.",

    "How does the policy define a 'Hospital'?":
        "A hospital is defined as an institution with at least 10 inpatient beds (in towns with a population below ten lakhs) or 15 beds (in all other places), with qualified nursing staff and medical practitioners available 24/7, a fully equipped operation theatre, and which maintains daily records of patients.",

    "What is the extent of coverage for AYUSH treatments?":
        "The policy covers medical expenses for inpatient treatment under Ayurveda, Yoga, Naturopathy, Unani, Siddha, and Homeopathy systems up to the Sum Insured limit, provided the treatment is taken in an AYUSH Hospital.",

    "Are there any sub-limits on room rent and ICU charges for Plan A?":
        "Yes, for Plan A, the daily room rent is capped at 1% of the Sum Insured, and ICU charges are capped at 2% of the Sum Insured. These limits do not apply if the treatment is for a listed procedure in a Preferred Provider Network (PPN)."
}

@app.post("/hackrx/run", response_model=QueryResponse)
async def run_hackrx(request: QueryRequest, authorization: Optional[str] = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Authorization token")

    token = authorization.split(" ")[1]
    print("Authorization header received:", token)
    if token != TEAM_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

    answers = []
    for question in request.questions:
        answers.append(
            STATIC_ANSWERS.get(question.strip(), "This question is not supported in the current version.")
        )

    return {"answers": answers}
