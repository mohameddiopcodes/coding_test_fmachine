## Engineering Code Test
a command line application written in python3 :
#
Test by running `test.sh` in the root directory
#
    sh test.sh


Run `print_solution.py` at the root to generate an output
#
    python3 print_solution.py
#
### Notable helper functions:
- `utilities/open_file`: reads files and outputs an array of lines

    #

        - last_name, first_name, gender, favorite_color, date_of_birth
        - last_name | first_name | middle_initial | gender| favorite_color | date_of_birth
        - last_name first_name middle_initial gender date_of_birth favorite_color

- `utilities/sanitize`: cleans data and outputs correct format.
    #					
        last_name first_name gender date_of_birth favorite_color

-  `utilities/generate_output`: sorts the data in 3 different ways to generate `solution`'s output:
    #
    1. sorted by gender and last name ascending:
        #   
            Output1:
            Hingis Martina Female 4/2/1979 Green
            Kournikova Anna Female 6/3/1975 Red
            Seles Monica Female 12/2/1973 Black
            Abercrombie Neil Male 2/13/1943 Tan
            Bishop Timothy Male 4/23/1967 Yellow
            Bonk Radek Male 6/3/1975 Green
            Bouillon Francis Male 6/3/1975 Blue
            Kelly Sue Male 7/12/1959 Pink
            Smith Steve Male 3/3/1985 Red
    2. sorted by birth date and last name ascending:
        #
            Output 2:
            Abercrombie Neil Male 2/13/1943 Tan
            Kelly Sue Male 7/12/1959 Pink
            Bishop Timothy Male 4/23/1967 Yellow
            Seles Monica Female 12/2/1973 Black
            Bonk Radek Male 6/3/1975 Green
            Bouillon Francis Male 6/3/1975 Blue
            Kournikova Anna Female 6/3/1975 Red
            Hingis Martina Female 4/2/1979 Green
            Smith Steve Male 3/3/1985 Red
    3. sorted by last name descending:
        #
            Output 3:
            Smith Steve Male 3/3/1985 Red
            Seles Monica Female 12/2/1973 Black
            Kournikova Anna Female 6/3/1975 Red
            Kelly Sue Male 7/12/1959 Pink
            Hingis Martina Female 4/2/1979 Green
            Bouillon Francis Male 6/3/1975 Blue
            Bonk Radek Male 6/3/1975 Green
            Bishop Timothy Male 4/23/1967 Yellow
            Abercrombie Neil Male 2/13/1943 Tan

### Thanks for reading through! 😁
