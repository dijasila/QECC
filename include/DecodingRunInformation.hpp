//
// Created by lucas on 21/06/22.
//
#ifndef QUNIONFIND_DECODINGRUNINFORMATION_HPP
#define QUNIONFIND_DECODINGRUNINFORMATION_HPP
#include "Decoder.hpp"

#include <nlohmann/json.hpp>

using json = nlohmann::json;

enum DecodingResultStatus {
    SUCCESS, // estimated correctly up to stabilizer
    FAILURE  // logical operator introduced
    //FLAGGED_ERROR // not implemented
};
NLOHMANN_JSON_SERIALIZE_ENUM(DecodingResultStatus, {{SUCCESS, "success"},
                                                    {FAILURE, "failure"}})
/**
 * Contains information about a single run of a decoder
 * status determines whether the estimate is valid or not
 * result contains information obtained from the decoder
 */
struct DecodingRunInformation {
    double               physicalErrR = 0.0;
    std::size_t          codeSize     = 0U;
    gf2Vec               error        = {};
    gf2Vec               syndrome     = {};
    DecodingResultStatus status{};
    DecodingResult       result{};
    [[nodiscard]] json   to_json() const {
          return json{
                {"physicalErrRate", physicalErrR},
                {"codeSize", codeSize},
                {"error", Utils::getStringFrom(error)},
                {"syndrome", Utils::getStringFrom(syndrome)},
                {"decodingResult", result.to_json()},
                {"decodingStatus", status}};
    }

    void from_json(const json& j) {
        j.at("physicalErrRate").get_to(physicalErrR);
        j.at("codeSize").get_to(codeSize);
        j.at("error").get_to(error);
        j.at("syndrome").get_to(syndrome);
        j.at("decodingStatus").get_to(status);
    }

    [[nodiscard]] std::string toString() const {
        std::stringstream ss{};
        return this->to_json().dump(2U);
    }
};
#endif //QUNIONFIND_DECODINGRUNINFORMATION_HPP
