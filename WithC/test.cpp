template<typename T>
T g(T x, T y) {
  return x + y;
}

extern "C" {
    double g_double(double x, double y) { return g(x, y); }
    int g_int(int x, int y) { return g(x, y); }
}
