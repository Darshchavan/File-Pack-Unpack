from flask import Flask, render_template, request, redirect, url_for, flash
import os
from pack_unpack import Packer, Unpacker

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/pack', methods=['GET', 'POST'])
def pack():
    if request.method == 'POST':
        folder_name = request.form.get('folder_name')
        pack_file = request.form.get('pack_file')
        if not folder_name or not pack_file:
            flash("Please provide both folder name and packed file name!", "danger")
            return redirect(url_for('pack'))

        if not os.path.exists(folder_name):
            flash("The specified folder does not exist!", "danger")
            return redirect(url_for('pack'))

        try:
            packer = Packer()
            packer.pack(folder_name, pack_file)
            flash(f"Packed files successfully into {pack_file}!", "success")
        except Exception as e:
            flash(f"Error: {e}", "danger")
        return redirect(url_for('pack'))

    return render_template('pack.html')

@app.route('/unpack', methods=['GET', 'POST'])
def unpack():
    if request.method == 'POST':
        pack_file = request.form.get('pack_file')
        if not pack_file:
            flash("Please provide the packed file path!", "danger")
            return redirect(url_for('unpack'))

        if not os.path.exists(pack_file):
            flash("The specified packed file does not exist!", "danger")
            return redirect(url_for('unpack'))

        try:
            unpacker = Unpacker()
            unpacker.unpack(pack_file)
            flash(f"Unpacked files successfully from {pack_file}!", "success")
        except Exception as e:
            flash(f"Error: {e}", "danger")
        return redirect(url_for('unpack'))

    return render_template('unpack.html')

if __name__ == "__main__":
    app.run(debug=True)
