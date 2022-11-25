# -*- coding: utf-8 -*-
"""1M_Movie_Ratings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XWLxPshIGrcSmUMdM1qTF9WcUbfWDzEw
"""

from mrjob.job import MRJob
from mrjob.job import MRStep

class RatingsBreakdown(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
            reducer=self.reducer_count_ratings)
    ]
# note that the splitting is now changed to '::' instead of '\t' because data is now seperated by :: in the new file.
    def mapper_get_ratings(self, _, line):
      (userID, movieID, rating, timestamp) = line.split('::')
      yield rating, 1

    def reducer_count_ratings(self, key, values):
      yield key, sum(values)

if __name__ == '__main__':
    RatingsBreakdown.run()