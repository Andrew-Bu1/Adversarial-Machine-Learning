from art.attacks.evasion import ZooAttack
from base_attack import BaseAttack

class ZooAttack(BaseAttack):
    def __init__(self, classifier, targeted=True):
        self.model = ZooAttack(classifier=classifier, targeted=targeted)

    def generate(self, x, y):
        return self.model.generate(x, y) 

