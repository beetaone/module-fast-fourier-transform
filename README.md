# Fast Fourier Transform

|           |                                                                                                     |
| --------- | --------------------------------------------------------------------------------------------------- |
| Name      | Fast Fourier Transform                                                                              |
| Version   | v1.0.1                                                                                              |
| DockerHub | [beetaone/fast-fourier-transform](https://hub.docker.com/r/beetaone/fast-fourier-transform) |
| Authors   | Jakub Grzelak                                                                                       |

- [Fast Fourier Transform](#fast-fourier-transform)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the beetaone Agent on the edge-node](#set-by-the-beetaone-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Extract elementary frequencies and magnitudes from your data.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on beetaone platform:

| Name        | Environment Variables | type   | Description                                                                                                              |
| ----------- | --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------ |
| Input Label | INPUT_LABEL           | string | Label of data to apply FFT to.                                                                                           |
| Sample Data | SAMPLE_SIZE           | string | Number of samples taken per second, sample rate of 1024 means that 1024 values of the signal are recorded in one second. |

### Set by the beetaone Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by beetaone agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| EGRESS_URLS           | string | HTTP ReST endpoints for the next module        |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
scipy
numpy
```

## Input

Input to this module is a single JSON object with is bytes object containing compressed (LZMA compression) array of data points of a simulated waveform.:

## Output

Output of this module is list of the detected frequencies and magitudes, formatted as a list of objects;

```json
[
    {
        "frequency": 270,
        "magnitude": 2
    },
    {
        "frequency": 60,
        "magnitude": 25
    }
]
```