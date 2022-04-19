import pytest
from app import schemas


def test_get_all_posts(client, init_posts):
    res = client.get("/")
    # print(res.json())
    assert res.status_code == 200
    
def test_get_one_post(client, init_posts):
    res = client.get(f"/{init_posts[0].id}")

    post = res.json()

    assert res.status_code == 200
    assert post['id'] == init_posts[0].id
    assert post['title'] == init_posts[0].title
    assert post['content'] == init_posts[0].content


def test_get_one_post_not_exist(client, init_posts):
    res = client.get("/23499994")
    assert res.status_code == 404


@pytest.mark.parametrize(
    "title, content, published",
    [
        ("Intro to FastAPI", "test content 2", True),
        ("Writing Tests", "test content 2, Tests", False),
        ("What is Web 3.0? ", "test content 2 about web 3", True),
    ],
)
def test_create_post(client, init_posts, title, content, published):
    res = client.post(
        "/", json={"title": title, "content": content, "published": published}
    )

    new_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert new_post.title == title
    assert new_post.content == content
    assert new_post.published == published


def test_create_post_published_true(client):
    res = client.post(
        "/", json={"title": "Test post published true", "content": "published?, yes"}
    )

    new_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert new_post.title == "Test post published true"
    assert new_post.content == "published?, yes"
    assert new_post.published == True


def test_delete_post(client, init_posts):
    res = client.delete(f"/{init_posts[0].id}")
    assert res.status_code == 204


def test_delete_post_non_exist(client):
    res = client.delete(f"/8000000")

    assert res.status_code == 404


def test_update_post(client, init_posts):
    data = {
        "title": "updated title",
        "content": "updated content",
        "id": init_posts[0].id,
    }

    res = client.put(f"/{init_posts[0].id}", json=data)

    updated_post = schemas.Post(**res.json())

    assert res.status_code == 200
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]


def test_update_post_non_exist(client, init_posts):

    data = {
        "title": "updated title",
        "content": "updated content",
        "id": init_posts[3].id,
    }

    res = client.put(f"/000000", json=data)

    assert res.status_code == 404
