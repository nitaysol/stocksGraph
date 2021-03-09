if __name__ == "__main__":
    file = open('stocks.txt', 'r')
    lines = file.readlines()
    for line in lines:
        stock_name = line.strip()
        output_file = open(stock_name + ".html", 'a')
        output_file.write(" <title>" + stock_name + "</title>" + """
        <div class="tradingview-widget-container">
    <div id="tradingview_14ec1"></div>
    <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/OTC-""" + stock_name + """/" rel="noopener"
        target="_blank"><span class="blue-text">""" + stock_name + """ Chart</span></a> by TradingView</div>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
    <script type="text/javascript">
      new TradingView.widget({
        "width": 800,
        "height": 610,
        "symbol": "OTC:""" + stock_name + """ ",
        "timezone": "Etc/UTC",
        "theme": "dark",
        "style": "1",
        "locale": "en",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "hide_top_toolbar": true,
        "hide_legend": true,
        "withdateranges": true,
        "range": "5D",
        "studies": [
          "MACD@tv-basicstudies"
        ],
        "container_id": "tradingview_14ec1"
      });
    </script>
  </div>
        
        """)
        output_file.close()