def model_head_hidden_dense(model_input, model_output, outputs, model_settings):

    # Main input (image)
    inputs = [model_input]

    x = model_output

    # Add additional inputs with more data and concatenate
    if 'kmh' in settings.AGENT_ADDITIONAL_DATA:
        kmh_input = Input(shape=(1,), name='kmh_input')
        x = Concatenate()([x, kmh_input])
        inputs.append(kmh_input)

    # Add additional fully-connected layer
    x = Dense(model_settings['hidden_1_units'], activation='relu')(x)

    # And finally output (regression) layer
    predictions = Dense(outputs, activation='linear')(x)

    # Create a model
    model = Model(inputs=inputs, outputs=predictions)
    return model
