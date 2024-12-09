/* tslint:disable */
/* eslint-disable */
/**
 * FarmNote
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: yourmail@fhwn.ac.at
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import type {
  HTTPValidationError,
  Session,
} from '../models/index';
import {
    HTTPValidationErrorFromJSON,
    HTTPValidationErrorToJSON,
    SessionFromJSON,
    SessionToJSON,
} from '../models/index';

export interface JoinSessionRequest {
    token: string;
}

/**
 * 
 */
export class SessionApi extends runtime.BaseAPI {

    /**
     * Request a new session
     * Create Session
     */
    async getNewSessionRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Session>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/session/`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => SessionFromJSON(jsonValue));
    }

    /**
     * Request a new session
     * Create Session
     */
    async getNewSession(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Session> {
        const response = await this.getNewSessionRaw(initOverrides);
        return await response.value();
    }

    /**
     * get a session by ID
     * Get Session
     */
    async getSessionRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Session>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/session/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => SessionFromJSON(jsonValue));
    }

    /**
     * get a session by ID
     * Get Session
     */
    async getSession(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Session> {
        const response = await this.getSessionRaw(initOverrides);
        return await response.value();
    }

    /**
     * join a session and return all notes from the session
     * Join Session
     */
    async joinSessionRaw(requestParameters: JoinSessionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<any>> {
        if (requestParameters['token'] == null) {
            throw new runtime.RequiredError(
                'token',
                'Required parameter "token" was null or undefined when calling joinSession().'
            );
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/session/join/{token}`.replace(`{${"token"}}`, encodeURIComponent(String(requestParameters['token']))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        if (this.isJsonMime(response.headers.get('content-type'))) {
            return new runtime.JSONApiResponse<any>(response);
        } else {
            return new runtime.TextApiResponse(response) as any;
        }
    }

    /**
     * join a session and return all notes from the session
     * Join Session
     */
    async joinSession(requestParameters: JoinSessionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<any> {
        const response = await this.joinSessionRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
