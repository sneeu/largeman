# Largeman

[![Build
Status](https://travis-ci.org/sneeu/largeman.png?branch=develop)](https://travis-ci.org/sneeu/largeman)

A little library for making, and using state machines.


## Usage

    from largeman import StateMachine, State

    sm = StateMachine()
    sm.add_state('on')
    sm.add_state('off')

    sm.add_transition('on', 'turn_off', 'off')
    sm.add_transition('off', 'turn_on', 'on')

    s = State(sm, 'off')

    s.turn_on()
    assert s.current() == 'on'

    s.turn_off()
    assert s.current() == 'off'


## Install

    pip install largeman
