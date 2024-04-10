from flask import Flask, render_template, request
from flask_cors import CORS
from pyflowchart import Flowchart

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/convert', methods=['POST'])
def convert_to_html():
    data = request.json
    code = data['code']
    fc = Flowchart.from_code(code)
    print(fc.flowchart())

    code = '''<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Flowchart</title>
    <style type="text/css">
      body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
      }
      #canvas {
        margin: 20px auto;
        max-width: 800px;
        background-color: #fff;
        border-radius: 8px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        padding: 20px;
      }
      .flowchart-element {
        stroke: #4169E1; /* Blue outline color */
      }
      .flowchart-text {
        font-size: 14px;
        color: #333;
      }
      .flowchart-line {
        stroke: #4169E1; /* Blue line color */
        stroke-width: 2px;
      }
      .flowchart-end-element {
        fill: none;
      }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.3.0/raphael.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowchart/1.17.1/flowchart.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.1/js/bootstrap.bundle.min.js"></script>
    <script>
        window.onload = function () {
            var chart;

            function drawFlowchart() {
                var code = `'''+fc.flowchart()+'''`;

                if (chart) {
                  chart.clean();
                }

                chart = flowchart.parse(code);
                chart.drawSVG('canvas', {
                  'line-width': 3,
                  'line-length': 50,
                  'text-margin': 10,
                  'font-size': 14,
                  'font-color': '#333',
                  'line-color': '#4169E1', /* Blue line color */
                  'element-color': '#4169E1', /* Blue outline color */
                  'fill': 'none',
                  'yes-text': 'yes',
                  'no-text': 'no',
                  'arrow-end': 'block',
                  'scale': 1,
                  'symbols': {
                    'start': {
                      'font-size': 14,
                      'font-color': '#4169E1', /* Blue font color */
                      'element-color': '#4169E1', /* Blue outline color */
                      'class': 'flowchart-element'
                    },
                    'inputoutput': {
                      'font-color': '#333',
                      'element-color': '#4169E1', /* Blue outline color */
                      'class': 'flowchart-element'
                    },
                    'operation': {
                      'font-color': '#333',
                      'element-color': '#4169E1', /* Blue outline color */
                      'class': 'flowchart-element'
                    },
                    'subroutine': {
                      'font-color': '#333',
                      'element-color': '#4169E1', /* Blue outline color */
                      'class': 'flowchart-element'
                    },
                    'condition': {
                      'font-color': '#4169E1', /* Blue font color */
                      'element-color': '#4169E1', /* Blue outline color */
                      'class': 'flowchart-element'
                    },
                    'end':{
                      'font-size': 20,
                      'class': 'flowchart-end-element'
                    }
                  }
                });
            }

            // Draw flowchart initially
            drawFlowchart();
        };
    </script>
    </head>
    <body>
        <div id="canvas"></div>
    </body>
    </html>

    '''
    return code

if __name__ == '__main__':
    app.run(debug=True)
