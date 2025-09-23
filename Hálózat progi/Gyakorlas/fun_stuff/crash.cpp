#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdexcept>

int main() {
    // A karakterkódolás beállítása a magyar ékezetes karakterek helyes megjelenítéséhez
    #ifdef _WIN32
    system("chcp 65001 > nul");
    #endif

    try {
        // --- VÁLTOZTATÁS ---
        // A létrehozandó fájlok száma itt van fixen beállítva.
        const int c = 5;
        std::cout << c << " darab 1GB-os fájl létrehozása..." << std::endl;

        // Létrehozunk egy 1MB-os puffert (buffer) 'X' karakterekkel feltöltve.
        const size_t buffer_size = 1024 * 1024 * 10; // 100 MB
        std::vector<char> buffer(buffer_size, 'X');

        for (int i = 0; i < c; ++i) {
            int ib = i + 1;
            std::string name = "Sziauram" + std::to_string(ib) + ".txt";
            
            std::ofstream fp(name, std::ios::binary);

            if (fp.is_open()) {
                std::cout << "\nFájl létrehozva: " << name << std::endl;

                // 100-szor írjuk ki az 1MB-os puffert, hogy 100MB legyen a fájlméret.
                for (int j = 0; j < 100; ++j) {
                    fp.write(buffer.data(), buffer.size());
                    std::cout << "\r  -> " << name << " írása: " << j + 1 << "%" << std::flush;
                }
                std::cout << std::endl;

            } else {
                std::cerr << "Hiba a fájl létrehozásakor: " << name << std::endl;
            }
        }

    } catch (const std::exception& e) {
        std::cerr << "Hiba történt: " << e.what() << std::endl;
    }

    std::cout << "\nA program befejezte a futást." << std::endl;
    return 0;
}