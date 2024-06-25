from classes.model import Model
from algorithms.randomise import *

import copy
import random


class HillClimber:
    """
    The HillClimber class that changes a random route in the model to random valid route. Each imporvement
    or equivalent solution is kept for the next iteration.
    """
    def __init__(self, model: Model) -> None:
        self.model = copy.deepcopy(model)
        self.score = model.calculate_score()

    def mutate_single_route(self, new_model: Model):
        """
        Changes the stations of a random route to random stations
        """
        random_route_id = random.choice(list(new_model.routes))
        random_reconfigure_route(new_model, random_route_id)
        # random_reconfigure_route(new_model, rand_route_2)

    def mutate_two_routes(self, new_model: Model):
        """
        Changes the stations of a random route to random stations
        """
        random_route_id, rand_route_2 = random.sample(list(new_model.routes),2)
        random_reconfigure_route(new_model, random_route_id)
        random_reconfigure_route(new_model, rand_route_2)


    def mutate_end_of_routes(self, new_model: Model):
        """
        Randomly removes some stations from the end of two routes. Then will only extend the first route.
        """
        random_route_id = random.choice(list(new_model.routes))
        for _ in range(random.randint(1,3)):
            new_model.get_route(random_route_id).remove_last_station()

        random_route_id_2 = random.choice(list(new_model.routes))
        for _ in range(random.randint(1,3)):
            new_model.get_route(random_route_id_2).remove_last_station()

        new_model.update_used_connections()
        if new_model.get_route(random_route_id).get_stations():
            random_extend_route(new_model, random_route_id)
        else:
            start_station = new_model.stations[random.choice(new_model.get_stations_unused_connections())]
            random_single_route(new_model, start_station, random_route_id)

    def delete_routes(self, new_model: Model):

        route_1, route_2 = random.sample(list(new_model.routes), 2)
        new_model.remove_route(route_1)
        new_model.remove_route(route_2)
        start_station = new_model.stations[random.choice(new_model.get_stations_unused_connections())]
        random_single_route(new_model, start_station, route_1)

    def reorder_single_route(self, new_model: Model, route_id = None):
        """
        Reorders the route using only the stations already in the route.
        """
        if route_id is None:
            route_id = random.choice(list(new_model.routes))

        random_reorder_route(new_model, route_id)


    def check_score(self, new_model: Model):
        """
        Checks and accepts better scoring models than the current model
        """
        new_score = new_model.calculate_score()
        old_score = self.score


        # accept equal and higher scores
        if new_score >= old_score:
            self.model = new_model
            self.score = new_score

    def run(self, iterations: int):
        """
        Runs the HillCLimber for a given number of iterations.
        """
        self.iterations = iterations
        # method_frequencies = {self.mutate_single_route: 2,
        #                         self.mutate_end_of_routes: 3,
        #                         self.delete_routes: 1,
        #                         self.reorder_single_route: 2}
        # # Create the method list based on frequencies
        # method_list = []
        # for method, frequency in method_frequencies.items():
        #     method_list.extend([method] * frequency)



        for iteration in range(iterations):

            # print(f'Iteration {iteration}/{iterations}, current value: {self.score}')

            # create copy of the model to simulate the change
            new_model = self.model.copy()

            # pick which change to make from parameters
            method = random.choice([self.mutate_two_routes, 
                                    self.mutate_end_of_routes, self.delete_routes, self.delete_routes,
                                    self.mutate_end_of_routes, self.reorder_single_route])


            method(new_model)

            self.check_score(new_model)

        # after hillclimber is done iterate routes to reorder to the fastest versions of the routes
        for route in self.model.routes:
            for iteration in range(1000):

                print(f'Reorder route{route}: {iteration}/{1000}, current value: {self.score}')

                # create copy of the model to simulate the change
                new_model = self.model.copy()

                # pick which change to make from parameters
                self.reorder_single_route(new_model, route)

                self.check_score(new_model)


