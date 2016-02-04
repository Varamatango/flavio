import unittest
import numpy as np
from .classes import *

class TestClasses(unittest.TestCase):
    def test_parameter_class(self):
        p = Parameter( 'm_b' )
        self.assertEqual( p, Parameter.get_instance('m_b') )
        p.set_description('b quark mass')
        self.assertEqual( p.get_description(), 'b quark mass' )
        d = NormalDistribution(4.2, 0.2)
        p.add_constraint( d )
        # checking central values
        self.assertEqual( p.get_central(), 4.2)
        self.assertEqual( d.get_central(), 4.2)
        # checking types and shapes of random values
        self.assertEqual( type(d.get_random()), float)
        self.assertEqual( d.get_random(3).shape, (3,))
        self.assertEqual( d.get_random((4,5)).shape, (4,5))
        self.assertEqual( type(p.get_random()), np.float64)
        self.assertEqual( p.get_random(3).shape, (3,))
        self.assertEqual( p.get_random((4,5)).shape, (4,5))
        # removing dummy instances
        del Parameter._instances['m_b']

    def test_observable_class(self):
        o = Observable( 'test_obs' )
        self.assertEqual( o, Observable.get_instance('test_obs') )
        o.set_description('some test observables')
        self.assertEqual( o.get_description(), 'some test observables' )
        # removing dummy instances
        del Observable._instances['test_obs']

    def test_prediction_class(self):
        o = Observable( 'test_obs' )
        p = Parameter( 'test_parameter' )
        def f(par_dict, wc_obj):
            return par_dict['test_parameter']*2
        pr  = Prediction( 'test_obs', f )
        wc_obj = None
        p.add_constraint( NormalDistribution(1.2, 0.1) )
        self.assertEqual( pr.get_central(wc_obj), 2.4)
        self.assertEqual( o.prediction_central(wc_obj), 2.4)
        # removing dummy instances
        del Observable._instances['test_obs']
        del Parameter._instances['test_parameter']