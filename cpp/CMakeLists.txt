cmake_minimum_required(VERSION 3.10)
project(LLMInferenceEngine VERSION 1.0)

# Enforce C++17 standard for modern features
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Attempt to find OpenMP for multithreading
find_package(OpenMP)

# Define the main executable
add_executable(run src/run.cpp)

# Point the compiler to your header files
target_include_directories(run PRIVATE include)

# Apply aggressive CPU optimization flags
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(run PRIVATE 
        -O3             # Maximum optimization for speed
        -march=native   # Optimize instructions for your specific CPU architecture
        -ffast-math     # Allow aggressive floating-point optimizations
    )
endif()

# Link OpenMP if it was found on the system
if(OpenMP_CXX_FOUND)
    target_link_libraries(run PUBLIC OpenMP::OpenMP_CXX)
endif()