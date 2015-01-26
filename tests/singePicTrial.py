import os
import sys
import random
sys.path.append('..')
import nude
import imp

def randomPathSampler(w, h):
    # print [(x,y) for x in range(w) for y in range(h)]
    yield random.choice([(x,y) for x in range(w) for y in range(h)])

def testfile(fname, resize=False):
    #n = nude.Nude(fname, randomPathSampler)
    n = nude.Nude(fname)
    if resize:
        n.resize(maxheight=800, maxwidth=600)
    n.parse()
    return n.result


def testAll():
    nudePath = os.path.join('samples', 'nude')
    notNudePath = os.path.join('samples', 'not_nude')
    nudeFile = os.path.join('samples', 'nude',
                random.choice(os.listdir(nudePath)))
    notNudeFile = os.path.join('samples', 'not_nude',
            random.choice(os.listdir(notNudePath)))
    print nudeFile, testfile(nudeFile)
    print notNudeFile, testfile(notNudeFile)

if __name__ == '__main__':
    # print randomPathSampler(4,54).next()
    testAll()
