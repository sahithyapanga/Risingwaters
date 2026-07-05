try:
    rainfall = float(request.form["rainfall"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    river_level = float(request.form["river_level"])

    data = np.array([[rainfall, temperature, humidity, river_level]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "⚠️ High Flood Risk"
    else:
        result = "✅ Low Flood Risk"

    return render_template("result.html", prediction=result)

except Exception as e:
    return render_template("result.html", prediction=f"Error: {e}")
