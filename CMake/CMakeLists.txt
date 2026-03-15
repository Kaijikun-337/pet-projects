cmake_minimum_required(VERSION 3.11)

project(MyGame)

# 1. Fetch the FTXUI library from GitHub automatically
include(FetchContent)
FetchContent_Declare(ftxui
  GIT_REPOSITORY https://github.com/ArthurSonzogni/FTXUI
  GIT_TAG        v5.0.0
)
FetchContent_MakeAvailable(ftxui)

# 2. Create your executable
add_executable(Game main.cpp)

# --- STATIC LINKING MAGIC ---
if(WIN32)
    # Tell GCC to bake the standard libraries INSIDE the exe
    target_link_options(Game PRIVATE 
        -static-libgcc 
        -static-libstdc++ 
        -static
    )
endif()

# 3. Link the library to your game
target_link_libraries(Game PRIVATE ftxui::screen ftxui::dom ftxui::component)

# 4. Use C++17 (Required for FTXUI)
set_property(TARGET Game PROPERTY CXX_STANDARD 17)

# Link Windows Sockets (ws2_32)
target_link_libraries(Game PRIVATE ws2_32)