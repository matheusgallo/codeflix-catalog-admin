from src.core.category.application.create_category_repository import CreateCategoryRepository


class InMemoryCategoryRepository(CreateCategoryRepository):
  def __init__(self, categories=None):
    self.categories = categories or []

  def save(self, category):
    self.categories.append(category)