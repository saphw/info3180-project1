"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from app.forms import UploadForm
import os
from werkzeug.utils import secure_filename
from app.models import propertyData

path = app.config['UPLOAD_FOLDER']
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties')
def propertyList():
    """Render the website's properties page."""
    properties= db.session.query(Property).all()
    return render_template('properties.html',properties=properties)
#return render_template('properties.html')


@app.route('/properties/<int:propertyid>')
def propertyView():
    #Render the website's property page.
    property = db.session.query(Property).get(propertyid)
    return render_template('property.html', property=property)

#Render the website's create new properties form.
@app.route('/properties/create', methods=['GET','POST'])
def newProperty():
    property= UploadForm()
    if request.method== 'POST' and property.validated():
       file= property.dp.data
       filename= secure_filename(file.filename)
       file.save(os.path.join(path, filename))

       newProp = propertyData(
            request.form['title'],
            request.form['bedrooms'],
            request.form['bathrooms'],
            request.form['location'],
            request.form['price']
           
       )

       db.session.add(newProp)
       db.session.commit()

       flash("Propert Added", 'sucess')
       return redirect(url_for('propertes'))
    return render_template("properties_create.html", form=property)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
