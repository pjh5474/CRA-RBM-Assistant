from app.repositories.bigquery_repository import BigQueryRepository


class AnalyticsService:
    def __init__(self):
        self.repository = BigQueryRepository()

    def get_overview(self):
        return self.repository.get_overview()

    def get_yearly(self):
        return self.repository.get_yearly()

    def get_countries(self, limit: int = 20):
        return self.repository.get_countries(limit)

    def get_condition_trend(self, condition: str):
        return self.repository.get_condition_trend(condition)
