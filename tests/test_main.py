from analysis.price_analysis import analyze_prices


def test_analysis():

    prices = [100, 200, 300]

    result = analyze_prices(prices)

    assert result["Lowest Price"] == 100

    assert result["Highest Price"] == 300

    assert result["Average Price"] == 200
