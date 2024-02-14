from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestCreateCategory: 
  def test_create_category_with_valid_data(self):
    repository = InMemoryCategoryRepository()
    use_case = CreateCategory(repository=repository)
    request = CreateCategoryRequest(
      name="Filme", 
      description="Filmes disponíveis", 
      is_active=True
    )

    response = use_case.execute(request)

    created_category = repository.categories[0]

    assert created_category.id == response.id
    assert created_category.name == request.name
    assert created_category.description == request.description
    assert created_category.is_active is True



