from simulator.core.core import run
from simulator.core.sim_state import State
from simulator.plugins import plugin1
from simulator.utils.config import setup_params
from simulator.utils.output import output_state


def main(fname):
    params = setup_params(fname)
    state = State(params)
    output_state(state)
    run(state, plugins=[plugin1.run])
    output_state(state)
