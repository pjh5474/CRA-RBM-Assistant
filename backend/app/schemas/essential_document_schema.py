from typing import List, Optional
from pydantic import BaseModel


class EssentialDocumentResponse(BaseModel):
    documentId: str
    studyId: str
    siteId: str
    documentType: str
    required: bool
    status: str
    version: Optional[str] = None
    documentDate: Optional[str] = None
    expiryDate: Optional[str] = None
    comment: Optional[str] = None


class EssentialDocumentReadinessResponse(BaseModel):
    studyId: str
    siteId: str
    siteName: str
    readinessScore: int
    totalDocuments: int
    readyDocuments: int
    missingDocuments: int
    pendingDocuments: int
    expiredDocuments: int
    documents: List[EssentialDocumentResponse]
