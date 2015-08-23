from nose.tools import *
from algs.array_funcs import *
from random import randint
import numpy as np


def maketestarray(size,range='default',n=0):
    if type(size)==type(int()):
        size=[size]
    if range=='bounded':
        return np.random.randint(n,size=size)
    if range=='default':
        return np.random.randint(-10*sum(size),high=10*sum(size),size=size)
    if range=='bool':
        return np.random.randint(2,size=size)


def test_maxdiff():
    test1=[5,4,3,2,1,0,-1,-2,-3,-4,-5] # should return 0
    test2=[0,1,2,3,4,5,6,7,8,9,10] # should return 10
    test3=[5,4,3,2,1,0,1,2,3,4,5,4,3,2,1] # should return 5
    tests=[test1,test2,test3]
    answers=[0,10,5]
    for i in xrange(len(tests)):
        test=tests[i]
        answer=answers[i]
        assert_equal(answer,maxdiff_bruteforce(test))
        assert_equal(answer,maxdiff_merge(test))
        assert_equal(answer,maxdiff_fast(test))


def test_maxdiff_2():
    test1=[5,4,3,2,1,0,-1,-2,-3,-4,-5] # should return 0
    test2=[0,1,2,3,4,5,6,7,8,9,10] # should return 10
    test3=[5,4,3,2,1,0,1,2,3,4,5,4,3,2,1] # should return 5
    test4=[1,2,3,0,1,2,3,4,5,0,1,2,3,4,5] # should return 10
    tests=[test1,test2,test3,test4]
    answers=[0,10,5,10]
    for i in xrange(len(tests)):
        test=tests[i]
        answer=answers[i]
        assert_equal(answer,maxdiff_2_bruteforce(test))
        assert_equal(answer,maxdiff_2_fast(test))


def test_increasing_subarray():
    test1=np.array([0]) # should return [0,0]
    test2=np.array([0,0,1,2,3,4,5,5]) # should return [1,6]
    test3=np.array([0,1,2,3,0,1,2,3]) # should return [4,7]
    tests=[test1,test2,test3]
    answers=[[0,0],[1,6],[4,7]]
    for i in xrange(len(tests)):
        test=tests[i]
        answer=answers[i]
        assert_equal(longest_increasing_subarray(test),answer)
        assert_equal(longest_increasing_subarray_(test),answer)


def test_weak_equivalence():
    n=10
    A=[3,6,3,2,9,4]
    B=[2,2,9,9,8,7]
    answer=[0,1,2,2,4,5,2,4,2,2]
    assert_equal(weak_equivalence(n,A,B).tolist(),answer)
    assert_equal(weak_equivalence_(n,A,B).tolist(),answer)

    n=10
    A=[]
    B=[]
    answer=[0,1,2,3,4,5,6,7,8,9]
    assert_equal(weak_equivalence(n,A,B).tolist(),answer)
    assert_equal(weak_equivalence_(n,A,B).tolist(),answer)

    n=10
    A=[1,4,5,7,7,0]
    B=[2,3,2,6,2,9]
    answer=[0,1,1,3,3,1,1,1,8,0]
    assert_equal(weak_equivalence(n,A,B).tolist(),answer)
    assert_equal(weak_equivalence_(n,A,B).tolist(),answer)


def test_reversearray():
    for i in xrange(100):
        test=maketestarray(100)
        reversed=reversearray(test.copy())
        print reversed
        for i in xrange(len(test)):
            assert_equal(test[i], reversed[len(test)-1-i])


def test_rotatearray():
    for i in xrange(100):
        size=10
        test=maketestarray(size)
        shift_amt=randint(0,size-1)
        rotated=rotatearray(test.copy(), shift_amt)
        print shift_amt
        print test
        print rotated
        for i in xrange(len(test)):
            assert_equal(test[i], rotated[(i+shift_amt)%size])



