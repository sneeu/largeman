class StateMachine(object):
    def __init__(self):
        self._states = set()
        self._transitions = {}

    def add_state(self, state_name):
        self._states.add(state_name)

    def add_transition(self, name, from_state, to_state):
        assert name not in self._transitions.keys()
        assert from_state in self._states
        assert to_state in self._states

        self._transitions[name] = (from_state, to_state)

    @property
    def states(self):
        return self._states

    @property
    def transitions(self):
        return set(self._transitions.keys())
