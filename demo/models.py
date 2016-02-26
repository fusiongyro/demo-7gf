from sqlalchemy import Column, Index, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    title  = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    isbn   = Column(Integer, primary_key=True)
    loans  = relationship("Loan", back_populates="book")

    def lend_to(self, borrower):
        self.loans.add(Loan(self, borrower))

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    isbn = Column(Text, ForeignKey('books.isbn'), nullable=False)
    borrower = Column(Text, nullable=False)
    borrowed_at = Column(DateTime, nullable=False, server_default='current_timestamp')
    returned_at = Column(DateTime)
    book = relationship("Book", back_populates="loans")

    def __init__(self, book, borrower):
        (self.book, self.borrower) = (book, borrower)
        self.borrowed_at = DateTime()

