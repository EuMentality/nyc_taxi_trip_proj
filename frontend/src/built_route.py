import folium
import osmnx as ox
import networkx as nx


def find_shortest_route(start_coords: tuple[float, float],
                        end_coords: tuple[float, float],
                        place: str = 'Manhattan, New York, United States',
                        mode: str = 'drive',
                        optimizer: str = 'length') -> folium.folium.Map:
    """Function finds the optimal route between two objects by coordinates on the map.
    :param start_coords: Сoordinates of the start of the trip 
    :param end_coords: Сoordinates of the end of the trip 
    :param place: Trip area
    :param mode: Type of trip - bike, drive, walk
    :param optimizer: Optimization goal, time or length
    :return: Shortes route map
    """
    graph = ox.graph_from_place(place, network_type = mode)
    orig_node = ox.get_nearest_node(graph, start_coords)
    dest_node = ox.get_nearest_node(graph, end_coords)
    shortest_route = nx.shortest_path(graph, source=orig_node, target=dest_node, weight=optimizer)
    shortest_route_map = ox.plot_route_folium(graph, shortest_route, tiles='openstreetmap', route_color='#6495ED')
    start_marker = folium.Marker(location = start_coords, icon = folium.Icon(color='green'), popup='Start')
    end_marker = folium.Marker(location = end_coords, icon = folium.Icon(color='red'), popup='End')
    start_marker.add_to(shortest_route_map)
    end_marker.add_to(shortest_route_map)
    return shortest_route_map
