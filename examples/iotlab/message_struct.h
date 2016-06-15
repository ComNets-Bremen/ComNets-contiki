#ifndef MESSAGE_STRUCT_H
#define MESSAGE_STRUCT_H

struct measure_message {
    uint32_t seq;
    uint16_t temperature;
    uint16_t humidity;
    uint16_t light1;

};

#endif /* MESSAGE_STRUCT_H */
