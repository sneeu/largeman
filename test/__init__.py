try:
    import unittest2 as unittest
except ImportError:
    import unittest

from largeman import InvalidState, InvalidTransition, StateMachine


class StateMachineTestCase(unittest.TestCase):
    def setUp(self):
        self.sm = StateMachine()
        self.sm.add_state('on')
        self.sm.add_state('off')

    def test_create_states(self):
        sm = self.sm
        self.assertEqual(sm.states, set(['on', 'off']))

    def test_create_transitions(self):
        sm = self.sm
        sm.add_transition('on', 'turn_off', 'off')
        sm.add_transition('off', 'turn_on', 'on')

        self.assertEqual(sm.states, set(['on', 'off']))
        self.assertEqual(
            sm.transitions, set([('on', 'turn_off', ), ('off', 'turn_on', )]))

    def test_invalid_states(self):
        sm = self.sm

        self.assertRaises(
            InvalidState, sm.add_transition, 'not_state', 'ignore',
            'not_state2')

        self.assertRaises(
            InvalidState, sm.add_transition, 'on', 'ignore',
            'not_state')

    def test_invalid_transition(self):
        sm = self.sm

        sm.add_transition('on', 'ignore', 'on')
        self.assertRaises(
            InvalidTransition, sm.add_transition, 'on', 'ignore', 'off')


class StateTestCase(unittest.TestCase):
    def setUp(self):
        self.sm = StateMachine()
        self.sm.add_state('on')
        self.sm.add_state('off')
        self.sm.add_transition('on', 'turn_off', 'off')
        self.sm.add_transition('off', 'turn_on', 'on')

    def test_create_state(self):
        state = self.sm('on')
        self.assertEqual(state.current, 'on')

        state2 = self.sm('off')
        self.assertEqual(state2.current, 'off')

    def test_transition(self):
        state = self.sm('on')
        self.assertEqual(state.current, 'on')

        state.turn_off()
        self.assertEqual(state.current, 'off')

        self.assertRaises(InvalidTransition, state.turn_off)

        state.turn_on()
        self.assertEqual(state.current, 'on')

    def test_available_transitions(self):
        state = self.sm('on')

        self.assertEqual(state.available_transitions(), ['turn_off'])

        state.turn_off()

        self.assertEqual(state.current, 'off')
        self.assertEqual(state.available_transitions(), ['turn_on'])
