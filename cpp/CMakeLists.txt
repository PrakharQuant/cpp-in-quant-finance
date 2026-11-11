cmake_minimum_required(VERSION 3.14)
project(QuantFinanceExamples LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Monte Carlo European call
add_executable(monte_carlo_call monte_carlo_call.cpp)
target_compile_options(monte_carlo_call PRIVATE -O3 -Wall -Wextra -pedantic)

# Order book aggregator
add_executable(order_book order_book.cpp)
target_compile_options(order_book PRIVATE -O3 -Wall -Wextra -pedantic)
