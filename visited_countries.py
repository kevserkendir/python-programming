def show_visited_countries(visited_countries):
    """ Show all the countries that were visited."""
    print("\nThe following countries have been visited:")
    for visited_countries in visited_countries:
        print(visited_countries)

unvisited_countries = ['netherlands','iceland', 'poland','colombia']
visited_countries = []
print_countries(unvisited_countries, visited_countries)
show_visited_countries(visited_countries)
