import platform
import subprocess

from flask import Flask, render_template, jsonify, request

from OS_scripts.linux import arp_scan_linux, arp_scan_nmap_linux
from OS_scripts.windows import arp_scan_windows, arp_scan_nmap_windows
from utils.administrative_utils import is_sudo_linux
from utils.menu_utils import run_nmap_scan_big_web

app = Flask(__name__)


@app.route('/')
def home():
    """Home page route"""
    if platform.system() == "Linux":
        sudo_status = is_sudo_linux()
    else:
        sudo_status = None
    return render_template('index.html', sudo_status=sudo_status)


@app.route('/api/arp_scan')
def api_arp_scan():
    try:
        if platform.system() == "Windows":
            arp_scan = arp_scan_windows()
        else:
            arp_scan = arp_scan_linux()
        return jsonify({"success": True, "results": arp_scan})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/arp_scan')
def arp_scan_page():
    """ARP Scan page route"""
    # arp_scan_ = arp_scan()
    # return render_template('arp_scan.html', arp_scan=arp_scan_)
    return render_template("arp_scan.html")


@app.route('/api/arp_scan_nmap')
def api_arp_scan_nmap():
    try:
        ip = request.args.get('ip')
        if not ip:
            return jsonify({"success": False, "error": "IP address is required."})

        if platform.system() == "Windows":
            arp_scan_nmap = arp_scan_nmap_windows(ip)
        else:
            arp_scan_nmap = arp_scan_nmap_linux(ip)

        return jsonify({"success": True, "results": arp_scan_nmap})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/arp_scan_nmap')
def arp_scan_nmap_page():
    """ARP Scan Nmap page route"""
    return render_template('arp_scan_nmap.html')


@app.route('/api/arp_scan_nmap_big')
def api_arp_scan_nmap_big():
    try:
        ip = request.args.get('ip')
        if not ip:
            return jsonify({"success": False, "error": "IP address is required."})

        arp_scan_nmap_big = run_nmap_scan_big_web(ip)

        return jsonify({"success": True, "results": arp_scan_nmap_big})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/arp_scan_nmap_big')
def arp_scan_nmap_big_page():
    """ARP Scan Nmap Big page route"""
    return render_template('arp_scan_nmap_big.html')


# this dont support any stop button, so we have to use improved string
# @app.route('/api/flood_ping')
# def api_flood_ping():
#     try:
#         ip = request.args.get('ip')
#         if not ip:
#             return jsonify({"success": False, "error": "IP address is required."})
#
#         if platform.system() == "Windows":
#             flood_ping = flood_ping_windows(ip)
#         else:
#             flood_ping = flood_ping_linux(ip)
#
#         return jsonify({"success": True, "results": flood_ping})
#     except Exception as e:
#         return jsonify({"success": False, "error": str(e)})


processes = {}


@app.route('/api/flood_ping/start')
def start_flood_ping():
    """Start flood ping process"""
    if platform.system() == "Windows":
        return jsonify({
            "success": False,
            "error": "Flood ping is not supported on your operating system. Learn more at "
                     "<a href='/switch_linux'>this link</a>."
        })

    ip = request.args.get('ip')
    if not ip:
        return jsonify({"success": False, "error": "IP address is required."})

    try:
        # Start the flood ping process
        process = subprocess.Popen(["ping", "-f", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process_id = process.pid
        processes[process_id] = process
        return jsonify({"success": True, "processId": process_id})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/api/flood_ping/stop')
def stop_flood_ping():
    process_id = request.args.get('processId')
    if not process_id:
        return jsonify({"success": False, "error": "Process ID is required."})

    try:
        process_id = int(process_id)
        process = processes.pop(process_id, None)
        if process:
            process.terminate()
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "error": "Process not found."})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route('/flood_ping')
def flood_ping_page():
    """Flood Ping page route"""
    return render_template('flood_ping.html')





@app.route('/switch_sudo')
def switch_sudo():
    """Switch Sudo page route"""
    if platform.system() == "Linux":
        sudo_status = is_sudo_linux()
    else:
        sudo_status = None
    return render_template('switch_sudo.html', sudo_status=sudo_status)


@app.route('/switch_linux')
def switch_linux():
    """Switch Linux page route"""
    return render_template('switch_linux.html')


@app.route('/result')
def result():
    """Result page route"""
    return render_template('result.html')


@app.route('/scan')
def scan():
    return render_template('scan.html')


@app.route('/history')
def history():
    """History page route"""
    return render_template('history.html')


@app.route('/cli')
def cli():
    """CLI page route"""
    return render_template('cli.html')


@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=8668, host="0.0.0.0")
