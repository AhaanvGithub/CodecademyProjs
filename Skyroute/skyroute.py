from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
stations_under_construction = []
for key, value in landmark_choices.items():
    landmark_string += "{0} ==> {1}\n".format(key, value)


def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)


def set_start_and_end(start_point, end_point):
    if start_point is not None:
        change_point = input("What would you like to change? type 'o' to change the origin, 'd' to change the "
                             "destination, or 'b' for both: \n")

        if change_point == 'b':
            start_point = get_start()
            end_point = get_end()
        elif change_point == 'o':
            start_point = get_start()
        elif change_point == 'd':
            end_point = get_end()
        else:
            print("Uh oh! That wasn't any of the available options.")
            set_start_and_end(start_point, end_point)
    else:
        start_point = get_start()
        end_point = get_end()
        if start_point != end_point:
            return start_point, end_point
        else:
            print("You cant have your destination and origin be the same!")
            set_start_and_end(start_point, end_point)


def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter:\n")
    if start_point_letter in landmark_choices.keys():
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, we don't have info on that landmark at the moment;")
        return get_start()


def get_end():
    end_point_letter = input("Ok, where are you headed? Type in the corresponding letter:\n")
    if end_point_letter in landmark_choices.keys():
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, we don't have info on that landmark at the moment;")
        return get_end()


def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if len(stations_under_construction) > 0 else vc_metro
            if len(stations_under_construction) > 0:
                possible_route = dfs(metro_system, start_station, end_station)
                if not possible_route:
                    return None
            route = bfs(metro_system, start_station, end_station)
            if route:
                routes.append(route)
    shortest_route = min(routes, key=len)
    return shortest_route


def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    if shortest_route:
        shortest_route_string = ""
        for i in range(len(shortest_route)):
            shortest_route_string += "{0} ==> ".format(shortest_route[i])
        print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
    else:
        print("Unfortunately, there is no path at the moment between {0} and {1} due to maintenance".format(start_point, end_point))
    again = input("Would you like to see another route? Enter y/n:\n")
    if again == "y":
        show_landmarks()
        new_route(start_point, end_point)


def get_active_stations():
    updated_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(stations_under_construction)
            else:
                updated_metro[current_station] = set([])

    return updated_metro


def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n:\n")
    if see_landmarks == "y":
        print(landmark_string)


def goodbye():
    print("Thanks for using SkyRoute!")


def skyroute():
    greet()
    new_route()
    goodbye()


skyroute()
