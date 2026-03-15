#include <ftxui/dom/elements.hpp>
#include <ftxui/component/component.hpp>
#include <ftxui/component/screen_interactive.hpp>
#include <winsock2.h> // Windows Sockets
#include <ws2tcpip.h>
#include <iostream>
#include <string>

#pragma comment(lib, "Ws2_32.lib")

using namespace ftxui;

// --- NETWORK CLASS ---
class NetworkClient {
    SOCKET sock;
public:
    NetworkClient() {
        WSADATA wsaData;
        WSAStartup(MAKEWORD(2, 2), &wsaData); // Init Windows Sockets
        sock = socket(AF_INET, SOCK_STREAM, 0);
    }

    bool connectToServer() {
        sockaddr_in server;
        server.sin_family = AF_INET;
        server.sin_port = htons(8080);
        inet_pton(AF_INET, "127.0.0.1", &server.sin_addr);

        if (connect(sock, (struct sockaddr*)&server, sizeof(server)) < 0) {
            return false;
        }
        return true;
    }

    void sendData(std::string msg) {
        send(sock, msg.c_str(), msg.length(), 0);
    }

    ~NetworkClient() {
        closesocket(sock);
        WSACleanup();
    }
};

int main() {
    NetworkClient net;
    std::string status = "Disconnected";
    int counter = 0;

    // Connect automatically
    if (net.connectToServer()) {
        status = "Connected to Server";
    } else {
        status = "Server Not Found (Run server.py!)";
    }

    // --- UI LOGIC ---
    auto increase = [&] { 
        counter++; 
        net.sendData("Count is: " + std::to_string(counter)); 
    };

    auto btn_inc = Button("+ Increase & Send", increase);
    auto btn_quit = Button("Quit", [&] { exit(0); });

    auto container = Container::Vertical({
        btn_inc,
        btn_quit
    });

    auto renderer = Renderer(container, [&] {
        return vbox({
            text("NETWORKED CLICKER") | bold | center,
            separator(),
            text(status) | color(status[0] == 'C' ? Color::Green : Color::Red),
            text("Count: " + std::to_string(counter)),
            separator(),
            btn_inc->Render() | center,
            btn_quit->Render()
        }) | border;
    });

    auto screen = ScreenInteractive::FitComponent();
    screen.Loop(renderer);

    return 0;
}