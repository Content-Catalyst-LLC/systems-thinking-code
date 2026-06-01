package main
import ("encoding/csv"; "fmt"; "os"; "path/filepath")
func clamp(x, lo, hi float64) float64 { if x < lo { return lo }; if x > hi { return hi }; return x }
func main() {
    outDir := filepath.Join("outputs", "tables"); _ = os.MkdirAll(outDir, 0755)
    path := filepath.Join(outDir, "go_professional_scenario_scan.csv")
    f, err := os.Create(path); if err != nil { panic(err) }; defer f.Close()
    w := csv.NewWriter(f); defer w.Flush()
    _ = w.Write([]string{"article_slug", "pressure_reduction", "capacity_investment", "final_stock", "final_risk"})
    for pr := 0.0; pr <= 0.5001; pr += 0.10 { for ci := 0.0; ci <= 3.0001; ci += 0.50 {
        stock := float64(80); capacity := float64(49); burden := float64(42)
        for year := 0; year <= 30; year++ {
            pressure := (4.7 + 2.1*float64(year)*0.45) * (1.0 - pr)
            burden = clamp(burden + pressure*0.08 - ci*0.35, 0, 100)
            capacity = clamp(capacity + ci - burden*0.015, 0, 100)
            stock = clamp(stock + stock*0.025 - pressure - burden*0.035 + capacity*0.025, 0, 120)
        }
        risk := clamp(100 - (0.45*stock + 0.35*capacity - 0.20*burden), 0, 100)
        _ = w.Write([]string{"shifting-the-burden", fmt.Sprintf("%.2f", pr), fmt.Sprintf("%.2f", ci), fmt.Sprintf("%.2f", stock), fmt.Sprintf("%.2f", risk)})
    } }
    fmt.Println("Go professional scenario scan written:", path)
}
