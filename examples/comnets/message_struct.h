#ifndef MESSAGE_STRUCT_H
#define MESSAGE_STRUCT_H

struct measure_message {
    uint32_t seq;
    float bat_voltage;
    uint16_t temperature;
    uint16_t humidity;
    uint16_t light1;
    uint16_t light2;
};

#endif /* MESSAGE_STRUCT_H */
