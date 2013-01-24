import unittest2

from largeman import StateMachine


class StateMachineTestCase(unittest2.TestCase):
    def test_create_states(self):
        sm = StateMachine()
        sm.add_state('on')
        sm.add_state('off')

        self.assertEqual(sm.states, set(['on', 'off']))

    def test_create_transitions(self):
        sm = StateMachine()
        sm.add_state('on')
        sm.add_state('off')
        sm.add_transition('turn_off', 'on', 'off')
        sm.add_transition('turn_on', 'off', 'on')

        self.assertEqual(sm.states, set(['on', 'off']))
        self.assertEqual(sm.transitions, set(['turn_off', 'turn_on']))
