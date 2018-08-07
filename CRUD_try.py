# CRUD.py

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///douban.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)

class DoubanVideo(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    year = Column(Integer)
    reviews = relationship("DoubanReview", backref="reviews")

    def __repr__(self):
        return "<DoubanVideo(name='%s', year='%s')>" % (
                self.name, self.year)

class DoubanReview(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    user = Column(String)
    star = Column(Integer)
    vote = Column(Integer)
    comment = Column(String)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    # movies = relationship("DoubanVideo", backref="movies")

    def __repr__(self):
        return "<DoubanReview(user='%s', star='%s', vote='%s', comment='%s')>" % (
                self.user, self.star, self.vote, self.comment)

def create_video(name, year):
    session = Session()

    video = DoubanVideo(name=name, year=year)

    session.add(video)
    session.commit()

def get_video(name):
    # pass
    session = Session()
    
    videos = session.query(DoubanVideo).filter(DoubanVideo.name == name)
    for video in videos:
        print(video.name, video.year)
    return video.id

def update_video(name):
    # pass
    session = Session()
    
    videos = session.query(DoubanVideo).filter(DoubanVideo.name == name)

    for video in videos:
        print(video.name, video.year)
        video.year = int(input('input the year of the movie: '))
        print('updated')
        print(video.name, video.year)
     
    session.commit()   

    return videos                                   

def delete_video(name):
    session = Session()

    videos = session.query(DoubanVideo).filter(DoubanVideo.name == name)

    for video in videos:
        session.delete(video)
    session.commit()

def create_review(movie, user, star, vote, comment):
    # pass
    session = Session()

    review = DoubanReview(user=user, star=star, vote=vote, comment=comment, movie_id=get_video(movie))

    session.add(review)
    session.commit()

def get_review(movie, user):
    # pass
    session = Session()
                                      
    reviews = session.query(DoubanReview).filter_by(movie_id=get_video(movie), user=user) 
    for review in reviews:
        print('reviews:')
        print(review)
    return review

def update_review(movie, user, star, comment):
    # pass
    session = Session()

    reviews = session.query(DoubanReview).filter_by(movie_id=get_video(movie), user=user, star=star)

    for review in reviews:
        print(user, star, comment) 
        review.comment = input('input the new comment: ')                                        
    session.commit()                                                  

def delete_review(movie, user):
    # pass                                                  
    session = Session()

    reviews = session.query(DoubanReview).filter_by(movie_id=get_video(movie), user=user)

    for review in reviews:
        session.delete(review)
    session.commit()
    
# create_video("little sunshine", 2001)
# create_video("another movie", 2002)
# get_video("little sunshine")
# update_video("little sunshine")
# create_video('test', 2006)
# delete_video('test')
# create_review('little sunshine', 'user_a', 5, 150, 'I like it')
# create_review('little sunshine', 'user_b', 5, 10, 'I like it, too')
# get_review('little sunshine', 'user_b')
# update_review('little sunshine', 'user_a', 5, 'I love it')
# create_review('another movie', 'user_a', 5, 150, 'I like it')
# create_review('another movie', 'user_b', 5, 150, 'I like it')
# delete_review('another movie', 'user_b')
delete_video('another movie')