from flask import Flask, render_template_string, request,render_template
import time
import os




app = Flask(__name__)

@app.route('/')
def index():
    html_form = """
    <h1>Ping Tester</h1>
    <form method="post" action="/send_packets">
        <label for="packets_wanted">How much packets do you want?</label><br>
        <input type="number" id="packets_wanted" name="packets_wanted" value="4" min="1"><br><br>
        
        <label for="target_site">What site do you want to ping?</label><br>
        <input type="text" id="target_site" name="target_site" value="google.com" required><br><br>
'
        <input type="submit" value="Submit'">
    </form>
    
    when you press the button you are gonna accept to not use this tool for ddos attacks.  
    """
    return html_form

@app.route('/send_packets', methods=['POST'])
def send_packets():
    try:
        packets_wanted_str = request.form.get('packets_wanted')
        target_site = request.form.get('target_site')

        if not packets_wanted_str or not target_site:
            return  "<h1> ERROR 400 <h1>"  "Put a valid number of packet and a valid site url.", 400

        packets_wanted = int(packets_wanted_str)

        output = []
        output.append(f"Sending {packets_wanted} to {target_site}...")
        output.append("Please wait...")
        time.sleep(1)

        
        comando = f"ping -c {packets_wanted} {target_site}"
        
        # Utilizzo di os.popen per catturare l'output del comando
        with os.popen(comando) as pipe:
            for line in pipe:
                output.append(line.strip())
        
        return render_template_string("<h1>Result of thr Ping</h1><pre>{{ output|join('<br>') }}</pre>", output=output)

    except ValueError:
        return 
        "<h1> ERROR 400 <h1>"
        "This number of packets isn't valid.", 400
    except Exception as e:
        return f"ERROR: {e}", 500

if __name__ == '__main__':
    app.run(host='127.8.4.1', port=1000)
    app.run(debug=True)
