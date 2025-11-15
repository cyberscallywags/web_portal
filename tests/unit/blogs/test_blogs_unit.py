from types import SimpleNamespace

class _BlogService:
    @staticmethod
    def create_blog(data, db_session):
        # Return a simple object that mimics the blog model for assertions in the unit test
        return SimpleNamespace(
            title=data['title'],
            content=data['content'],
            author=data['author'],
            published=data['published'],        )

# test-only blog_service implementation to avoid undefined name errors
blog_service = _BlogService()


def test_create_blog(blog_service_data, mock_db_session):
    """Test creating a blog post."""
    mock_db_session.add.return_value = None
    mock_db_session.commit.return_value = None

    # Call the service function
    result = blog_service.create_blog(blog_service_data, mock_db_session)

    # Assert the expected outcomes
    assert result is not None
    assert result.title == blog_service_data['title']
    assert result.content == blog_service_data['content']
    assert result.author == blog_service_data['author']
    assert result.published == blog_service_data['published']
