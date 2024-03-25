#include "main.h"

void initializeRepository(CountryRepository* repository)
{
    addCountry(repository, "Romania", "Europe", 19, 0);
    addCountry(repository, "Greece", "Europe", 10, 0);
    addCountry(repository, "Bulgaria", "Europe", 6, 0);
    addCountry(repository, "Hungary", "Europe", 9, 0);
    addCountry(repository, "Slovakia", "Europe", 5, 0);
    addCountry(repository, "Austria", "Europe", 9, 0);
    addCountry(repository, "Czech Republic", "Europe", 10, 0);
    addCountry(repository, "Germany", "Europe", 83, 0);
    addCountry(repository, "France", "Europe", 67, 0);

    addCountry(repository, "India", "Asia", 1408, 0);
    addCountry(repository, "Bangladesh", "Asia", 169, 0);
    addCountry(repository, "Japan", "Asia", 125, 0);
    addCountry(repository, "South Korea", "Asia", 51, 0);
    addCountry(repository, "China", "Asia", 1412, 0);

    addCountry(repository, "United States", "America", 331, 0);
    addCountry(repository, "Canada", "America", 38, 0);
    addCountry(repository, "Mexico", "America", 126, 0);
    addCountry(repository, "Cuba", "America", 11, 0);
    addCountry(repository, "Brazil", "America", 214, 0);
}

int main()
{
    CountryRepository* repository = CreateCountryRepository();

    RunALlTests(repository);

    initializeRepository(repository);


    startMenu(repository);
    return 0;
}