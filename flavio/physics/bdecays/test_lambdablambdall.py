import unittest
import numpy as np
import flavio


wc_sm = flavio.WilsonCoefficients()
# choose parameters as required to compare numerics to arXiv:1602.01399
par_nominal = flavio.default_parameters.copy()
flavio.physics.bdecays.formfactors.lambdab_12.lattice_parameters.lattice_load_nominal(par_nominal)
par_nominal.set_constraint('Vcb', 0.04175)
par_dict = par_nominal.get_central_all()

def ass_sm(s, name, q2min, q2max, target, delta, scalef=1):
    obs = flavio.classes.Observable.get_instance(name)
    c = obs.prediction_central(par_nominal, wc_sm, q2min, q2max)*scalef
    s.assertAlmostEqual(c, target, delta=delta)

class TestLambdabLambdall(unittest.TestCase):
    def test_lambdablambdall(self):
        # first, make sure we use the same CKM factor as in arXiv:1602.01399 eq. (69)
        self.assertAlmostEqual(abs(flavio.physics.ckm.xi('t', 'bs')(par_dict)), 0.04088, delta=0.0001)
        # compare to table VII of 1602.01399
        ass_sm(self, '<dBR/dq2>(Lambdab->Lambdamumu)', 0.1, 2, 0.25, 0.01, 1e7)
        ass_sm(self, '<dBR/dq2>(Lambdab->Lambdamumu)', 2, 4, 0.18, 0.005, 1e7)
        ass_sm(self, '<dBR/dq2>(Lambdab->Lambdamumu)', 15, 20, 0.756, 0.002, 1e7)
        ass_sm(self, '<dBR/dq2>(Lambdab->Lambdamumu)', 18, 20, 0.665, 0.002, 1e7)