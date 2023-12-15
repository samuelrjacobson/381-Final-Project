from youtube import reviews_search

def test_reviews_search():
    reviews_list = reviews_search("Harry Potter")
    
    assert len(reviews_list) == 10  
    
    for review in reviews_list:
        assert not review['id'] == None
        assert not review['title'] == None
        assert not review['description'] == None
        
    assert "Harry Potter".upper() in str(reviews_list).upper()