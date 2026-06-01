package main

import "fmt"

func main() {
    graph := map[string][]string{
        "frontline_team": {"data_platform", "public_agency"},
        "maintenance_unit": {"funding_stream"},
        "regional_infrastructure": {"maintenance_unit", "ecological_context"},
        "community_users": {"regional_infrastructure", "public_agency"},
        "public_agency": {"oversight_body", "funding_stream"},
    }

    fmt.Println("Dependency pathway scaffold")
    for source, targets := range graph {
        for _, target := range targets {
            fmt.Printf("%s -> %s\n", source, target)
        }
    }
}
