
## IO
- Printing to a specific number of decimal points
    ```cpp
    #include <iostream>
    #include <iomanip>
    #include <cmath>
    
    using namespace std;
    
    int main() {
        cout << setprecision(6) << fixed;
        cout << M_PI << endl;
    }
    
    Outputs: 3.141593   
    ```
    
    `std::fixed` sets the default formatting for stdout
    
    `std::setprecision` sets the precision to be expected in a given i/o stream
    