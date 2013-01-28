class InvalidState(Exception):
    pass


class InvalidTransition(Exception):
    pass


class StateMachine(object):
    def __init__(self):
        self._states = set()
        self._transitions = {}

    def add_state(self, state_name):
        self._states.add(state_name)

    def add_transition(self, from_state, name, to_state):
        if from_state not in self._states:
            raise InvalidState(
                'from_state {0} not a valid state.'.format(from_state))

        if (from_state, name, ) in self._transitions:
            raise InvalidTransition(
                'transision {0}.{1} already exists.'.format(from_state, name))

        if to_state not in self._states:
            raise InvalidState(
                'to_state {0} not a valid state.'.format(to_state))

        self._transitions[from_state, name] = to_state

    def get_transition(self, from_state, name):
        return self._transitions[from_state, name]

    @property
    def states(self):
        return self._states

    @property
    def transitions(self):
        return set(self._transitions.keys())

    def __call__(self, initial):
        return State(self, initial)


class State(object):
    def __init__(self, machine, initial):
        self._machine = machine
        self._current = initial

    def _make_transition(self, name):
        transition = self._machine.get_transition(self._current, name)

        def __transition():
            self._current = transition

        return __transition

    def __getattr__(self, name):
        if (self._current, name, ) in self._machine.transitions:
            return self._make_transition(name)

    def available_transitions(self):
        return [t[1]
            for t in self._machine.transitions
            if t[0] == self.current]

    @property
    def current(self):
        return self._current
