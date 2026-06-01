package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"path/filepath"
)

func clamp(value, low, high float64) float64 {
	if value < low {
		return low
	}
	if value > high {
		return high
	}
	return value
}

func riskScore(condition, criticality, redundancy, cyberDependency float64) float64 {
	return clamp((100-condition)*0.35+criticality*0.30+(100-redundancy)*0.20+cyberDependency*0.15, 0, 100)
}

func main() {
	outPath := filepath.Join("outputs", "tables", "go_infrastructure_resilience_scores.csv")
	os.MkdirAll(filepath.Dir(outPath), 0755)

	file, err := os.Create(outPath)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	writer.Write([]string{"asset_id", "risk_score"})
	assets := []struct {
		id, category                         string
		condition, criticality, redundancy, cyber float64
	}{
		{"bridge_north", "transport", 64, 78, 35, 28},
		{"water_main_east", "water", 58, 86, 25, 34},
		{"substation_7", "power", 70, 92, 42, 66},
	}

	for _, asset := range assets {
		score := riskScore(asset.condition, asset.criticality, asset.redundancy, asset.cyber)
		writer.Write([]string{asset.id, fmt.Sprintf("%.3f", score)})
	}

	fmt.Println("Wrote", outPath)
}
